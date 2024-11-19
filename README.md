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
    total_repositories = 34,
    total_stargazers = 231,
    total_commits_current_year = 726,
    total_prs = 54,
    total_issues = 16,
    top_languages = {
        go = "27.4%",
        lua = "26.2%",
        python = "10.9%",
        shell = "8.2%",
        r = "7.4%",
        cuda = "5.1%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
