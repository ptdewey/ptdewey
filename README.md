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
    total_commits_current_year = 233,
    total_prs = 77,
    total_issues = 27,
    top_languages = {
        go = "29.8%",
        lua = "26.3%",
        python = "9.0%",
        r = "6.2%",
        nix = "4.5%",
        shell = "4.3%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
