# pre-commit-hooks

Collection of hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v1.0.0 # Use the ref you want to point at
  hooks:
      - id: detect-unencrypted-ansible-vault
  # -   id: ...
```

### Hooks available

#### `detect-unencrypted-ansible-vault`

Detects the presence of unencrypted ansible vaults keys in files matching the pattern `.*\.?vault(.ya?ml)?$`

-   .vault
-   abc.vault
-   vault.yml
-   vault.yaml
-   vars.vault.yml
-   vars.vault.yaml
