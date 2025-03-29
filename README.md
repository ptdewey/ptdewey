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
    total_stargazers = 267,
    total_commits_current_year = 121,
    total_prs = 66,
    total_issues = 18,
    top_languages = {
        go = "30.1%",
        lua = "22.7%",
        python = "9.9%",
        r = "6.8%",
        shell = "6.8%",
        cuda = "4.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
