
class Refresher
{
    constructor(onRefresh, every)
    {
        this.onRefresh  = onRefresh;
        this.every      = every;
        this.intervalID = 0;
        this.active     = false;
        document.addEventListener("visibilitychange", () => this.handleVisibilityChange);
    }

    handleVisibilityChange()
    {
        if (document.hidden)  this._off();
        else if (this.active) this.on(true);
    }

    _off()
    {
        clearInterval(this.intervalID);
        this.intervalID = 0;
    }

    off()
    {
        this.active = false;
        this._off();
    }

    on(doNow=false)
    {
        this.active = true;
        this._off();
        if (!document.hidden) {
            this.intervalID = setInterval(this.onRefresh, this.every);
            if (doNow) this.onRefresh();
        }
    }

    setEvery(every)
    {
        if (every != this.every) {
            this._off();
            this.every = every;
            this.on();
        }
    }
}

export default Refresher;
