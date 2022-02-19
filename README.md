
# Hashcat Rule Engine CLI (hcre)
A simple cli tool to parse hashcat rules provided as command line arguments, apply the rules to stdin and output to stdout.

## Setup

### From source
```
git clone git@github.com:KMikeeU/hcre.git
cd hcre 
python -m build
pip install ./dist/hcre-0.0.1-py3-none-any.whl
```

## Usage
hcre will load any hashcat compatible rule files specified as command line arguments, apply them to stdin and output the results on stdout. This can be used to transform or enhance wordlists for all types of bruteforcing or fuzzing while pentesting.

### Examples

#### Gobuster
```shell
cat directory-list.txt | hcre example.rule | gobuster dir -u http://localhost:8080/ -w - -x php
```

## Implemented rules
**NOTE**: Rules which have not yet been implemented will simply be ignored

- Nothing (**:**)
- Lowercase (**l**)
- Uppercase (**u**)
- Capitalize (**c**)
- Invert Capitalize (**C**)
- Toggle Case (**t**)
- Toggle At (**TN**)
- Reverse (**r**)
- Duplicate (**d**)
- Duplicate N (**pN**)
- Reflect (**f**)
- Rotate Left (**\{**)
- Rotate Right (**\}**)
- Append Character (**$X**)
- Prepend Character (**^X**)
- Purge (**@X**)
- Replace Character (**sXY**)

To see how any of these rules function, please refer to the official [hashcat rule documentation](https://hashcat.net/wiki/doku.php?id=rule_based_attack#implemented_compatible_functions).

