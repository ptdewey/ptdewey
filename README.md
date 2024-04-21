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
    total_repositories = 24,
    total_stargazers = 47,
    total_commits_current_year = 151,
    total_prs = 30,
    total_issues = 9,
    top_languages = {
        lua = "24.8%",
        go = "19.8%",
        python = "14.2%",
        r = "11.2%",
        shell = "9.1%",
        cuda = "8.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
