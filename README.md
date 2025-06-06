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
    total_stargazers = 290,
    total_commits_current_year = 204,
    total_prs = 75,
    total_issues = 27,
    top_languages = {
        go = "30.1%",
        lua = "24.8%",
        python = "10.0%",
        shell = "6.3%",
        r = "6.2%",
        nix = "4.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
