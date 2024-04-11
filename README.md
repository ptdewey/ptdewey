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
    total_repositories = 21,
    total_stargazers = 29,
    total_commits_current_year = 135,
    total_prs = 30,
    total_issues = 9,
    top_languages = {
        lua = "23.7%",
        go = "18.9%",
        python = "14.7%",
        r = "11.7%",
        shell = "9.4%",
        cuda = "9.2%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
