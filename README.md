<!--CONTENT_START-->
```lua
-- initialize user profile
local ptdewey = {}

-- user info
ptdewey.info = {
    name = "patrick dewey",
    education = {
        masters = "computer science @ virginia tech",
        bachelors = "computational modeling and data analytics @ virginia tech"
    },
    experience = {
        "software engineer",
        "data scientist",
        "computational scientist"
    },
    interests = {
        "analyzing real world data",
        "building robust machine learning models",
        "building highly performant applications",
        "computational linear algebra",
        "linux configuration and shell scripting",
        "neovim lua plugin development"
    }
}

-- user stats
ptdewey.stats = {
    total_repositories = 26,
    total_stargazers = 49,
    total_commits_current_year = 178,
    total_prs = 31,
    total_issues = 9,
    top_languages = {
        lua = "22.7%",
        go = "17.9%",
        python = "17.0%",
        r = "10.9%",
        shell = "9.8%",
        cuda = "8.0%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
