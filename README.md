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
    total_repositories = 35,
    total_stargazers = 201,
    total_commits_current_year = 576,
    total_prs = 46,
    total_issues = 13,
    top_languages = {
        go = "27.2%",
        lua = "27.0%",
        python = "11.4%",
        shell = "8.3%",
        r = "7.8%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
