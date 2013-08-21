 // // Roomies.Store = DS.Store.extend({
  // // revision: 12,
  // // adapter: 'DS.FixtureAdapter'
// // });
// 
 // Roomies.Store = DS.Store.extend({
  // revision: 12,
  // adapter: 'DS.DjangoTastypieAdapter.extend()'
// });

Roomies.store = DS.Store.create({
        revision: 11,
        adapter: DS.DjangoTastypieAdapter.extend()
 });