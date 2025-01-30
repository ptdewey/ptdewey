<!--CONTENT_START-->
```lua
-- user-profile.lua
local ptdewey = {}

-- user info
ptdewey.info = {
    name = "patrick dewey",
    education = {
        masters = "computer science at virginia tech",
        bachelors = "computational modeling and data analytics at virginia tech"
    }
}

-- user stats
ptdewey.stats = {
    total_repositories = 38,
    total_stargazers = 246,
    total_commits_current_year = 36,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "27.3%",
        lua = "23.5%",
        python = "10.4%",
        r = "7.1%",
        shell = "6.7%",
        cuda = "4.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
