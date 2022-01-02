import massive from 'massive';

(async function () {
  const db = await massive({});

  await db.query('SELECT id, val FROM one');
  await db.two.insert({
    id: 1,
    val: 'one'
  });

  let stuff = 'things';

  await db.query(`UPDATE two SET val = val || ${stuff}`);
  await db.one.destroy({'id >': 5});
})();
