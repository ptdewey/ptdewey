<!--CONTENT_START-->
```lua
-- initialize user profile
local ptdewey = {}

-- user info
ptdewey.info = {
    name = "patrick dewey",
    education = {
        masters = "computer science at virginia tech",
        bachelors = "computational modeling and data analytics at virginia tech"
    },
    experience = {
        "software engineering",
        "data science",
        "computational science"
    }
}

-- user stats
ptdewey.stats = {
    total_repositories = 27,
    total_stargazers = 49,
    total_commits_current_year = 196,
    total_prs = 31,
    total_issues = 9,
    top_languages = {
        lua = "22.0%",
        go = "17.3%",
        python = "16.5%",
        r = "11.8%",
        shell = "9.5%",
        cuda = "7.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
