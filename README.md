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
    total_stargazers = 256,
    total_commits_current_year = 69,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "28.5%",
        lua = "23.4%",
        python = "10.3%",
        r = "7.1%",
        shell = "7.0%",
        cuda = "4.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
