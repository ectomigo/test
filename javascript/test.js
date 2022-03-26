import massive from 'massive';

(async function () {
  const db = await massive({});

  await db.query('SELECT id, val FROM one');
  await db.two.insert({
    id: 1,
    val: 'one'
  });

  let id = 5;
  let stuff = 'things';

  await db.query(`UPDATE one SET val = 5 WHERE id = ${id}`);
  await db.query(`UPDATE two SET val = val || ${stuff} WHERE id = ${
    id
    + 1
  }`);
  await db.one.destroy({'id >': 5});
})();
