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
    total_stargazers = 294,
    total_commits_current_year = 206,
    total_prs = 76,
    total_issues = 27,
    top_languages = {
        go = "30.4%",
        lua = "25.1%",
        python = "9.2%",
        shell = "6.3%",
        r = "6.3%",
        nix = "4.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
