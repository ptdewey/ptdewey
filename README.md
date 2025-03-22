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
    total_stargazers = 258,
    total_commits_current_year = 87,
    total_prs = 65,
    total_issues = 17,
    top_languages = {
        go = "29.2%",
        lua = "22.6%",
        python = "10.2%",
        r = "6.9%",
        shell = "6.9%",
        cuda = "4.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
