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
    total_stargazers = 301,
    total_commits_current_year = 244,
    total_prs = 75,
    total_issues = 27,
    top_languages = {
        go = "32.4%",
        lua = "27.6%",
        python = "7.3%",
        r = "5.5%",
        nix = "4.9%",
        cuda = "4.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
