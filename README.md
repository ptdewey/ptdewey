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
    total_repositories = 46,
    total_stargazers = 289,
    total_commits_current_year = 203,
    total_prs = 75,
    total_issues = 27,
    top_languages = {
        go = "30.7%",
        lua = "25.3%",
        python = "9.3%",
        shell = "6.4%",
        r = "6.3%",
        cuda = "4.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
