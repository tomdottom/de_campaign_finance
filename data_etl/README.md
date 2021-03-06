# de_data_etl

A small package to help extract data from files downloaded from https://cfrs.elections.delaware.gov

Take xls (html table) as an input and outputs rows of json data.

## Dependency Installation

```
pip install -r requirements.txt
```

## Usage

### Printing to stdout

```
python extract_contribution_list.py ./example_data/input_file.xls
```

Or

```
cat ./example_data/input_file.xls | python extract_contribution_list.py
```

### Saving to new file

```
python extract_contribution_list.py ./example_data/input_file.xls ./example_data/output.txt
```

Or

```
cat ./example_data/input_file.xls | python extract_contribution_list.py > ./example_data/output.txt
```

## Testing

```
pip install test_requirements.txt
nosetests
```
