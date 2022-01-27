import pandas as pd
import pathlib

def load_raw(directory):
    
    csv_path = [loc for loc in subdir.iterdir() if str(loc).endswith('.csv')][0]
    edgelist = pd.read_csv(str(csv_path))

    return edgelist


def clean_edgelist(edgelist):

    head_column_name = [col for col in edgelist if 'START_ID' in col][0]
    head_type = head_column_name[10:-4]

    tail_column_name = [col for col in edgelist if 'END_ID' in col][0]
    tail_type = tail_column_name[8:-4]

    relation = f"{head_type}_to_{tail_type}"
    
    edgelist_out = pd.DataFrame(columns=['head', 'relation', 'tail'])
    edgelist_out['head'] = edgelist[head_column_name]
    edgelist_out['relation'] = relation
    edgelist_out['tail'] = edgelist[tail_column_name]

    return edgelist_out


if __name__ == '__main__':

    output = pd.DataFrame()
    
    raw_path = pathlib.Path('raw')
    for subdir in raw_path.iterdir():

        # Load raw data
        raw_edgelist = load_raw(subdir)

        # Create output edgelist
        output_edgelist = clean_edgelist(raw_edgelist)

        # Store
        output = output.append(output_edgelist)

    # Write to disk
    output.to_csv('edgelist.csv', index=False)
