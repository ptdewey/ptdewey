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
    total_repositories = 44,
    total_stargazers = 300,
    total_commits_current_year = 241,
    total_prs = 75,
    total_issues = 27,
    top_languages = {
        go = "32.2%",
        lua = "28.0%",
        python = "7.2%",
        r = "5.5%",
        nix = "4.9%",
        cuda = "4.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
