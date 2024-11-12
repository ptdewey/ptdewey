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
    total_stargazers = 228,
    total_commits_current_year = 670,
    total_prs = 54,
    total_issues = 15,
    top_languages = {
        go = "28.1%",
        lua = "26.7%",
        python = "11.1%",
        shell = "8.4%",
        r = "7.6%",
        cuda = "5.2%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
