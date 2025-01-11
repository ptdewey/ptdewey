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
    total_repositories = 37,
    total_stargazers = 241,
    total_commits_current_year = 20,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "26.7%",
        lua = "25.9%",
        python = "10.4%",
        shell = "7.8%",
        r = "7.1%",
        cuda = "4.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
