
import json

files = ['ddm_raw.geojson']

for f in files:
    try:
        with open(f, 'r') as fh:
            data = json.load(fh)
            count = len(data.get('features', []))
            print(f"File: {f}")
            print(f"Total Features: {count}")
            
            # Check first few for ddm_values
            valid_ddms = 0
            for i, feat in enumerate(data['features']):
                if 'ddm_values' in feat['properties'] and feat['properties']['ddm_values']:
                    valid_ddms += 1
                if i < 3:
                    print(f"Feature {i} keys: {feat['properties'].keys()}")
            
            print(f"Features with non-empty ddm_values: {valid_ddms}")

    except Exception as e:
        print(f"Error reading {f}: {e}")
