if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    #data[~((data.passenger_count == 0) | (data.trip_distance == 0))] #option2
    data = data[(data.passenger_count > 0) & (data.trip_distance > 0)]
    data['lpep_pickup_date'] = data.lpep_pickup_datetime.dt.date
    data.columns = (data.columns
                    .str.replace('ID','_id')
                    .str.lower()
    )
    data = data.reset_index(drop=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert (output.columns.isin(['vendor_id'])).any(), 'Error: column vendor_id not present the dataframe. Check your data'
    assert (output.passenger_count > 0).all() , 'Error: passenger count should be > 0. Check your data'
    assert (output.trip_distance > 0).all() , 'Error: trip distance should be > 0. Check your data'


