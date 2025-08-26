import requests
import os
from datetime import datetime

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
USERNAME = os.environ.get('USERNAME')
NLANGS = 5
IGNORE_LIST = ['Jupyter Notebook']

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
            stargazers {{
              totalCount
            }}
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

    total_stars = sum(repo['stargazers']['totalCount'] for repo in data['allRepositories']['nodes'])
    total_issues = data['issues']['totalCount']
    total_prs = data['pullRequests']['totalCount']
    total_commits = data['contributionsCollection']['totalCommitContributions']
    
    # Calculate total size for all languages across all repositories, excluding ignored languages
    total_language_size = sum(lang['size'] for repo in data['userRepositories']['nodes'] for lang in repo['languages']['edges'] if lang['node']['name'] not in IGNORE_LIST)
    
    # Aggregate language stats excluding ignored languages and calculate percentage
    language_stats = {}
    for repo in data['userRepositories']['nodes']:
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
        "total_repositories": data['allRepositories']['totalCount'],
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
