import requests
import os
from datetime import datetime

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
USERNAME = os.environ.get('USERNAME')
NLANGS = 5
IGNORE_LIST = ['Jupyter Notebook']
EXTRA_REPOS = ["arabica-social/arabica"]

def fetch_extra_repos(repos, nlangs):
    """Fetch stargazerCount + languages for org/extra repos by owner/name.

    Uses aliased repository() fields so all repos are fetched in a single
    GraphQL request. Returns node dicts shaped like userRepositories nodes
    so they can be merged into the existing star/language aggregation.
    Repos that are missing or inaccessible come back null and are skipped.
    """
    if not repos:
        return []

    url = 'https://api.github.com/graphql'
    headers = {"Authorization": "Bearer %s" % EXTRA_REPOS_TOKEN}

    fields = []
    for i, (owner, name) in enumerate(repos):
        alias = "repo%d" % i
        owner_safe = owner.replace('"', '\\"')
        name_safe = name.replace('"', '\\"')
        fields.append(
            '  %s: repository(owner: "%s", name: "%s") {\n'
            '    stargazerCount\n'
            '    languages(first: %d, orderBy: {field: SIZE, direction: DESC}) {\n'
            '      edges {\n'
            '        size\n'
            '        node {\n'
            '          name\n'
            '        }\n'
            '      }\n'
            '    }\n'
            '  }'
            % (alias, owner_safe, name_safe, nlangs)
        )

    query = "query ExtraRepos {\n" + "\n".join(fields) + "\n}\n"

    response = requests.post(url, json={'query': query}, headers=headers)
    response.raise_for_status()

    payload = response.json()
    if payload.get('errors'):
        for err in payload['errors']:
            print("GraphQL error fetching extra repo: %s" % err.get('message', err))

    data = payload.get('data') or {}
    nodes = []
    for i, (owner, name) in enumerate(repos):
        node = data.get("repo%d" % i)
        if node is None:
            print("Skipping %s/%s: not found or not accessible" % (owner, name))
            continue
        nodes.append(node)
    return nodes


def fetch_github_stats(username, nlangs):
    url = 'https://api.github.com/graphql'
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    current_year = datetime.now().year
    from_date = f"{current_year}-01-01T00:00:00Z"
    to_date = f"{current_year}-12-31T23:59:59Z"

    query = f"""
    query UserStats($login: String!) {{
      user(login: $login) {{
        contributionsCollection(from: "{from_date}", to: "{to_date}") {{
          totalCommitContributions
        }}
        pullRequests(first: 100) {{
          totalCount
        }}
        issues(first: 100) {{
          totalCount
        }}
        repositoriesContributedTo(first: 100, includeUserRepositories: true) {{
          totalCount
        }}
        allRepositories: repositories(first: 100) {{
          totalCount
          nodes {{
            stargazerCount
          }}
        }}
        userRepositories: repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {{
          totalCount
          nodes {{
            languages(first: {nlangs}, orderBy: {{field: SIZE, direction: DESC}}) {{
              edges {{
                size
                node {{
                  name
                }}
              }}
            }}
          }}
        }}
      }}
    }}
    """
    
    variables = {"login": username}
    
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    response.raise_for_status()
    
    data = response.json()['data']['user']

    extra_repo_nodes = fetch_extra_repos(EXTRA_REPOS, nlangs)

    total_stars = sum(repo['stargazerCount'] for repo in data['allRepositories']['nodes'])
    total_stars += sum(repo['stargazerCount'] for repo in extra_repo_nodes)
    total_issues = data['issues']['totalCount']
    total_prs = data['pullRequests']['totalCount']
    total_commits = data['contributionsCollection']['totalCommitContributions']
    
    # Calculate total size for all languages across all repositories, excluding ignored languages
    total_language_size = sum(lang['size'] for repo in data['userRepositories']['nodes'] for lang in repo['languages']['edges'] if lang['node']['name'] not in IGNORE_LIST)
    total_language_size += sum(lang['size'] for repo in extra_repo_nodes for lang in repo['languages']['edges'] if lang['node']['name'] not in IGNORE_LIST)
    
    # Aggregate language stats excluding ignored languages and calculate percentage
    language_stats = {}
    for repo in data['userRepositories']['nodes'] + extra_repo_nodes:
        for lang in repo['languages']['edges']:
            language_name = lang['node']['name']
            if language_name not in IGNORE_LIST:
                language_stats[language_name] = language_stats.get(language_name, 0) + lang['size']
    
    # Calculate percentages
    language_percentages = {lang: (size / total_language_size) * 100 for lang, size in language_stats.items()}

    # Sort languages by percentage in descending order
    sorted_language_percentages = sorted(language_percentages.items(), key=lambda item: item[1], reverse=True)

    # Format percentages and truncate to 2 decimal places, then add a percentage sign
    formatted_languages = {lang: f"{percent:.1f}%" for lang, percent in sorted_language_percentages[:nlangs]}

    return {
        "total_repositories": data['allRepositories']['totalCount'] + len(extra_repo_nodes),
        "total_stargazers": total_stars,
        "commits_current_year": total_commits,
        # "total_prs": total_prs,
        # "total_issues": total_issues,
        "top_languages": formatted_languages
    }

def dict_to_lua_table(username, d, indent=0, base_indent="  "):
    lua_str = f"{username}.stats = {{\n" if username else "{\n"
    inner_indent = base_indent * (indent + 1)
    items = []
    for key, value in d.items():
        if isinstance(value, dict):
            value = {k.lower(): v for k, v in value.items()}
            value_str = dict_to_lua_table("", value, indent + 1, base_indent)
        else:
            value_str = f'"{value}"' if isinstance(value, str) else str(value)
        key_str = f'{key}' if isinstance(key, str) else str(key)
        items.append(f'{inner_indent}{key_str} = {value_str}')
    lua_str += ',\n'.join(items)
    lua_str += f'\n{base_indent * indent}}}'
    return lua_str

def update_readme(stats):
    readme_path = 'README.md'
    content_path = 'content/content.txt'
    # Generate stats string in Lua table format with proper indentation
    stats_str = dict_to_lua_table(USERNAME, stats, base_indent="    ")

    # Check if content.txt exists and read its contents
    extra_content = ""
    if os.path.exists(content_path):
        with open(content_path, 'r', encoding='utf-8') as content_file:
            extra_content = content_file.read()

    with open(readme_path, 'r', encoding='utf-8') as file:
        readme_contents = file.read()

        # Find the start and end delimiters of the placeholder region
        start_delimiter = '<!--CONTENT_START-->'
        end_delimiter = '<!--CONTENT_END-->'

        start_index = readme_contents.find(start_delimiter)
        end_index = readme_contents.find(end_delimiter)

        if start_index != -1 and end_index != -1:
            stats_block = readme_contents[start_index + len(start_delimiter):end_index].strip()
            # Prepare the stats block in Lua syntax
            stats_str = '```lua\n' + extra_content + '\n' + stats_str + '\n\nreturn ptdewey\n```'

        # Replace the content between the delimiters with the new stats, including extra content
        if start_index != -1 and end_index != -1:
            new_readme_contents = (
                readme_contents[:start_index + len(start_delimiter)]
                + '\n'
                + stats_str
                + '\n'
                + readme_contents[end_index:]
            )

            with open(readme_path, 'w', encoding='utf-8') as file:
                file.write(new_readme_contents)
        else:
            print("Placeholder region not found in README.")

if __name__ == "__main__":
    stats = fetch_github_stats(USERNAME, NLANGS)
    update_readme(stats)
