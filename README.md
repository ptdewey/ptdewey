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
    total_repositories = 40,
    total_stargazers = 258,
    total_commits_current_year = 86,
    total_prs = 64,
    total_issues = 17,
    top_languages = {
        go = "29.1%",
        lua = "22.9%",
        python = "10.1%",
        r = "6.9%",
        shell = "6.9%",
        cuda = "4.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
