# Hooks for MlOps [W.I.P]

This folder has a collection of hooks that can be used to extend
the functionality of the MlOps CLI. It is a work in progress. 
We will be adding more hooks as we go along. But for now, is more 
a didactical project.

## 1-Conventional Commit

In this project, we are following the conventional commit message approach. This approach is suitable for a beginner because is easy to follow the guidelines. 
A conventional commit message has the following structure

```
prefix(optional scope): description

optional body

optional footer(s)
```


For example

```
feat: allow ml model to be trained on a different dataset
```

This indicates this commit introduces a new feature.

If you perform an isolated modification in the documentation (fixing 
a typo in the docstrings from a python method, creating an example etc) you should use the `docs` prefix.

```
docs: correct spelling on the docstrings
```


You can use any of the following prefixes

```
"feat","fix","ci","revert","model","docs","style","refactor","test" or "perf"
```

But don't be afraid of using the "wrong" prefix, it's ok to choose what you believe is more suitable 
for your case. 

### 1-a) How can I give context to my commits? Scope.

If you want to become a more advanced user you can use scope. The scope is a way to be more specific about what you are doing. Let's take a look at the following example

```
fix(model): remove the dependency on the sklearn library

Sklearn is not compatible with this model. Thus, we need to remove the dependency on sklearn.

```

### 1-b) How to draw attention to a specific commit?

Suppose you sent a pull-request containing several commits. How to communicate to reviewers that some commits should be carefully reviewed? That they need to read the entire message? One way to do this is to use the exclamation mark `!`.

Let's see  an example

```
fix!: remove pip 22.0.2 dependency

Changes present in this commit must be removed
after `pip-tools` team's solution regarding pip log bug 
be merged and released

Related to: https://github.com/jazzband/pip-tools/issues/1558

```

Let's take a look at another example

```
feat(model)!: implement a new model more efficiently


BREAKING CHANGE: This model can result in a **critical** performance loss
if the dataset is not well-represented. 

```

### 1-c) Resume: Table of prefixes and the corresponding descriptions 

Here we are going to show you two tables of prefixes and the corresponding descriptions. In the future, as we learn more about MlOps, we will keep adding more prefixes that we think are suitable for MlOps. 


This is the first table that is common to all Software Development Teams [2, 3]
| Prefix     | Title                    | Description                                                  |
| ---------- | ------------------------ | ------------------------------------------------------------ |
| `feat`     | Features                 | A new feature                                                |
| `fix`      | Bug Fixes                | A bug Fix                                                    |
| `docs`     | Documentation            | Documentation only changes                                   |
| `style`    | Styles                   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc) |
| `refactor` | Code Refactoring         | A code change that neither fixes a bug nor adds a feature    |
| `perf`     | Performance Improvements | A code change that improves performance                      |
| `test`     | Tests                    | Adding missing tests or correcting existing tests            |
| `build`    | Builds                   | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm) |
| `ci`       | Continuous Integrations  | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) |
| `chore`    | Chores                   | Other changes that don't modify src or test files            |
| `revert`   | Reverts                  | Reverts a previous commit                                    |


The next table represents to us our current understanding of which prefixes (commit types) should be 
incorporated in the previous table to improve the quality of code evolution in MlOps projects.


| Commit Type | Title    | Description                      |
| ----------- | -------- | -------------------------------- |
| `model`     | ML Model | Changes and/or create a ML model |


# References

[1]“Conventional Commits.” https://www.conventionalcommits.org/en/v1.0.0/ (accessed Jan. 31, 2022).

[2]T. Hombergs, “Writing Meaningful Commit Messages,” Feb. 22, 2021. https://reflectoring.io/meaningful-commit-messages/ (accessed Jan. 31, 2022).

[3] “Editing conventional-commit-types/README.md at master · pvdlg/conventional-commit-types,” GitHub. https://github.com/pvdlg/conventional-commit-types (accessed Feb. 02, 2022).

