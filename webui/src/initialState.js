
const initialState = {
    isLive: false,
    content: {
        status: {
            'host': '0.0.0.0',
            'port': 5000,
            'neighbors': [],
            'blockchain': {
                'length': 0
            },
            'wallet': {
                'address': null,
                'balance': null,
                'utxos': []
            }
        }
    }
};

export default initialState;
