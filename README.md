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
    total_commits_current_year = 218,
    total_prs = 77,
    total_issues = 27,
    top_languages = {
        go = "29.6%",
        lua = "24.7%",
        python = "9.0%",
        shell = "6.2%",
        r = "6.1%",
        nix = "4.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
