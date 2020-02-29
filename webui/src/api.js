import axios from 'axios';

const apiURL = "http://" + env.SERVER_NAME + "/api/";

export async function get(path, params)
{
    const reply = await axios.get(apiURL + path, {params});
    if (!reply.data) throw Error("No reply from server");
    return reply.data;
}

export async function post(path, data={})
{
    const reply = await axios.post(apiURL + path, data);
    if (!reply.data) throw Error("No reply from server");
    return reply.data;
}
