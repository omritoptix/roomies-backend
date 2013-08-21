Roomies.Router.map(function () {
	this.resource('roomies',{path: '/'}, function() {
		
	});
	});

Roomies.RoomiesRoute = Ember.Route.extend({
	model: function () {
		return Roomies.Apartment.find();
	}
});

Roomies.RoomiesIndexRoute = Ember.Route.extend({
	model: function () {
		return Roomies.Apartment.find();
	}
});
