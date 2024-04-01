# `rmfmt`

Resolve all Python code formatting conflicts.

## History And Motivation

Early Python code formatters had too many configuration options, leading to developer
conflicts when developers couldn't compromise on formatting conventions.

As a result,
[Black, the uncompromising Python code formatter](https://github.com/psf/black) was
created with intentionally few configuration options, under the assumption that
developers would accept The One Formatting Convention To Rule Them All, even if it
wasn't the exact convention they wanted.

But Black still had too many configuration options that lead to developer conflicts,
so [shed was created as a "maximally opinionated" autoformatting tool](https://github.com/Zac-HD/shed/),
following the convention over configuration approach.

However, using `shed` continues to lead to developer conflicts and contention.

Introducing...`rmfmt`! A Python formatter with no configuration options, no conventions
to follow, and a guarantee to resolve developer conflicts over code formatting.

## How Does It Work?

`rmfmt` works by removing all code content from Python sourcecode files, effectively
truncating the files to 0 bytes. Developers therefore cannot argue or fight over code
formatting conventions, giving them more free time to focus on more important issues,
like which text editor is better and which Linux distribution is the best one.

## Installation And Use

### Installation

```bash
poetry add --group=dev rmfmt
```

```bash
rmfmt.py [files or directories]
```

### Pre-commit Hooks

`.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/blag/rmfmt.git
    ref: 0.1.0
    hooks:
      - run_rmfmt
```

## Frequently Asked Questions (FAQ)

**Q: Are there any drawbacks to truncating source code files?**

**A:** Many, but we believe that the boost in developer productivity will make the
drawbacks worth it.

**Q: Wait, so this just deletes all of my code?**

**A:** Yes. But it leaves the files alone and your project file structure in place.

**Q: Will you feel bad at all if somebody installs this and deletes all of their code?**

**A:** Will I feel bad if somebody goes out of their way to install this, configures
their pre-commit configuration to run it, and runs it without any aforethought as to
the consequences? No.

**Q: Will you accept issues or pull requests?**

**A:** Sure, but PRs probably won't be merged for exactly one year since the latest release.

**Q: Wouldn't `truncfmt` have been a better project name?**

**A:** More accurate, sure, but not a better one.

**Q: Is this a serious project?**

**A:** If I put this question in an FAQ, do you really need to ask this question?

**Q: Should I use this at all?**

**A:** That's a private, personal choice, between a developer and their manager.

## License

WTFPL
