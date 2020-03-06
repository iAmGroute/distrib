
const initialState = {
    isLive: false,
    content: {
        status: {
            'host': '0.0.0.0',
            'port': 5000,
            'neighbors': [],
            'blockchain': [],
            'utxos': [],
            'balance': null
        }
    }
};

export default initialState;
