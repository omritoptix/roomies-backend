// Roomies.Apartment = DS.Model.extend({
	// title:DS.attr('string'),
	// isAvailable:DS.attr('boolean')
// });

// Roomies.Apartment.FIXTURES = [
 // {
 	// id:1,
 	// title:'hanita 44',
 	// isAvailable: true
 // },
 // {
 	// id:2,
 	// title: 'hanit 55',
 	// isAvailable: false
 // }
 // ];

Roomies.Apartment = DS.Model.extend({
	address:DS.attr('string')
});