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
    total_stargazers = 49,
    total_commits_current_year = 156,
    total_prs = 30,
    total_issues = 9,
    top_languages = {
        lua = "24.8%",
        go = "19.5%",
        python = "14.0%",
        r = "11.1%",
        shell = "10.0%",
        cuda = "8.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
