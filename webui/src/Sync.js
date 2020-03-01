import { get }   from "./api.js";
import Refresher from "./Refresher.js";

class Sync
{
    constructor(onUpdate)
    {
        this.onUpdate   = onUpdate;
        this.pending    = 0;
        this.maxPending = 5;
        this.refresher  = new Refresher(() => this.refresh(), 500);
        this.refresher.on();
    }

    async refresh()
    {
        if (this.pending < this.maxPending) {
            this.pending += 1;
            try {
                const reply = await get("status");
                this.refresher.setEvery(2500);
                this.onUpdate(reply);
            }
            catch (error) {
                this.refresher.setEvery(7500);
                console.warn(error);
            }
            finally {
                this.pending -= 1;
                if (this.pending < 0) this.pending = 0;
            }
        }
    }
}

export default Sync;
