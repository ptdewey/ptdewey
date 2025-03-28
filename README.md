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
    total_repositories = 41,
    total_stargazers = 261,
    total_commits_current_year = 119,
    total_prs = 66,
    total_issues = 17,
    top_languages = {
        go = "30.0%",
        lua = "23.0%",
        python = "9.9%",
        r = "6.8%",
        shell = "6.7%",
        cuda = "4.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
