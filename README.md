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
    total_commits_current_year = 674,
    total_prs = 54,
    total_issues = 15,
    top_languages = {
        go = "27.9%",
        lua = "26.9%",
        python = "11.2%",
        shell = "8.5%",
        r = "7.7%",
        cuda = "5.3%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
