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
    total_stargazers = 245,
    total_commits_current_year = 23,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "26.0%",
        lua = "25.2%",
        python = "10.1%",
        shell = "7.6%",
        r = "6.9%",
        cuda = "4.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
