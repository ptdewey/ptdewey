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
    total_repositories = 47,
    total_stargazers = 295,
    total_commits_current_year = 207,
    total_prs = 76,
    total_issues = 27,
    top_languages = {
        go = "29.7%",
        lua = "24.5%",
        python = "9.0%",
        shell = "6.2%",
        r = "6.2%",
        nix = "4.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
