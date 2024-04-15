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
    total_repositories = 23,
    total_stargazers = 35,
    total_commits_current_year = 144,
    total_prs = 30,
    total_issues = 9,
    top_languages = {
        lua = "25.0%",
        go = "18.6%",
        python = "14.5%",
        r = "11.4%",
        shell = "9.3%",
        cuda = "9.0%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
