<script>
  import { get }         from '../api.js';
  import BlockchainTable from './BlockchainTable.svelte';

  export let state;

  async function getFirstBlocks() {
    const from   = 0;
    const to     = Math.min(10, state.content.status.blockchain.length);
    const blocks = [];
    for (let i = from; i < to; i++) {
      blocks.push(await get('getBlock', {blockID: i, detailed: false}));
    }
    return blocks;
  }
  async function getLastBlocks() {
    const from   = state.content.status.blockchain.length - 1;
    const to     = Math.max(from - 10, -1);
    const blocks = [];
    for (let i = from; i > to; i--) {
      blocks.push(await get('getBlock', {blockID: i, detailed: false}));
    }
    return blocks;
  }
</script>

<BlockchainTable
  title   = "Showing first 10 blocks"
  promise = {getFirstBlocks()}
></BlockchainTable>
<BlockchainTable
  title   = "Showing last 10 blocks"
  promise = {getLastBlocks()}
></BlockchainTable>
