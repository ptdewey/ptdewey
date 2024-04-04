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
    total_repositories = 20,
    total_stargazers = 17,
    total_commits_current_year = 118,
    total_prs = 25,
    total_issues = 7,
    top_languages = {
        go = "22.4%",
        lua = "17.7%",
        python = "17.4%",
        r = "13.8%",
        shell = "11.0%",
        cuda = "10.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
