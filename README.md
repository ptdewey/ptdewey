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
    total_repositories = 48,
    total_stargazers = 299,
    total_commits_current_year = 222,
    total_prs = 77,
    total_issues = 27,
    top_languages = {
        go = "29.2%",
        lua = "25.9%",
        python = "8.8%",
        shell = "6.1%",
        r = "6.0%",
        nix = "4.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
