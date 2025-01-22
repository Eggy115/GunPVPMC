while True:
    name = "Glock-19"
    name = input(f"name | {name}: ")
    if name == "":
        name = "Glock-19"

    type = "Pistol"
    type = input(f"type | {type}:  ")
    if type == "":
        type = "Pistol"

    colour = "333836"
    colour = input(f"guncolor| {colour}: ")
    if colour == "":
        colour = "333836"

    colour2 = "3356726"
    colour2 = input(f"gunothercolor| {colour2}: ")
    if colour2 == "":
        colour2 = "3356726"

    ammo = "9x19mm"
    ammo = input(f"ammo | {ammo}: ")
    if ammo == "":
        ammo = "9x19mm"

    ammocolour = "FFC300"
    ammocolour = input(f"ammocolour | {ammocolour}: ")
    if ammocolour == "":
        ammocolour = "FFC300"

    capacity = "15"
    capacity = input(f"capacity | {capacity}: ")
    if capacity == "":
        capacity = "15"
    
    tag = "glock19"
    tag = input(f"tag | {tag}: ")
    if tag == "":
        tag = "glock19"

    capstag = "GLOCK19"
    capstag = input(f"uppertag | {capstag}: ")
    if capstag == "":
        capstag = "GLOCK19"

    reload = "500"
    reload = input(f"reload | {reload}: ")
    if reload == "":
        reload = "500"

    firerate = "0.25"
    firerate = input(f"delay | {firerate}: ")
    if firerate == "":
        firerate = "0.25"

    ammotype = "gold nugget"
    ammotype = input(f"ammo | {ammotype}: ")
    if ammotype == "":
        ammotype = "gold nugget"
    
    damage = "5"
    damage = input(f"damage | {damage}: ")
    if damage == "":
        damage = "5"

    cost = "500"
    cost = input(f"cost | {cost}: ")
    if cost == "":
        cost = "500"

    print("""
on rightclick:
	if player is holding leather horse armor:
		if name of event-item contains "<##""" + colour + """>""" + name + """ &6[&cReloading&6]":
			if {""" + tag + """.%line 5 of lore of player's held item%} = 0:
				stop
		if name of event-item is "<##""" + colour + """>""" + name + """":	
			set {_} to "%player%%random integer between 10000 and 99999%"
			set line 5 of lore of player's held item to "&6ID: &c%{_}%"
			set {""" + tag + """.%line 5 of lore of player's held item%} to """ + capacity + """
			set name of player's held item to "<##""" + colour + """>""" + name + """ &6[&c%{""" + tag + """.%line 5 of lore of player's held item%}%&6]"
		if name of event-item contains "<##""" + colour + """>""" + name + """":		
			
			set name of player's held item to "<##""" + colour + """>""" + name + """ &6[&c%{""" + tag + """.%line 5 of lore of player's held item%}%&6]"
			set line 1 of lore of player's held item to "&6Cartridge: &c%{""" + tag + """.%line 5 of lore of player's held item%}%&6/&c""" + capacity + """"
			set line 2 of lore of player's held item to "&6Reload Time: &c""" + reload +"""ms"
			set line 3 of lore of player's held item to "&6Damage: &c""" + damage +""""
			set line 4 of lore of player's held item to "&6Ammunition: &c""" + ammo + """"
			
			if {""" + tag + """.%line 5 of lore of player's held item%} > 0:
				if difference between {""" + tag + """cd.%player%} and now > """ + firerate + """ second:
					set {""" + tag + """cd.%player%} to now				
					remove 1 from {""" + tag + """.%line 5 of lore of player's held item%}	
					shoot snowball at speed 5
					edit bossbar "%player%" title to "&6""" + name + """: &c%{""" + tag + """.%line 5 of lore of player's held item%}%"
					set bossbar "%player%" value to {""" + tag + """.%line 5 of lore of player's held item%} * """ + str(100/int(capacity)) + """
					console command "/execute at %player% run tag @e[type=snowball,limit=1,sort=nearest] add """ + capstag + """"
					console command "/execute at %player% run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 3 2"
					push player in direction of player at speed -0.1
				
					set name of player's held item to "<##""" + colour + """>""" + name + """ &6[&c%{""" + tag + """.%line 5 of lore of player's held item%}%&6]"
					set line 1 of lore of player's held item to "&6Cartridge: &c%{""" + tag + """.%line 5 of lore of player's held item%}%&6/&c""" + capacity + """"
					set line 2 of lore of player's held item to "&6Reload Time: &c""" + reload +"""ms"
					set line 3 of lore of player's held item to "&6Damage: &c""" + damage +""""
					set line 4 of lore of player's held item to "&6Ammunition: &c""" + ammo + """"	
					
				else:
					send action bar "&6Wait before shooting!" to player
			else:
				
				if player has 1 """ + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """":
					set {_id} to line 5 of lore of player's held item
					set name of player's held item to "<##""" + colour + """>""" + name + """ &6[&cReloading&6]"
					set line 1 of lore of player's held item to "&6Cartridge: &c0&6/&c""" + capacity + """"
					set line 2 of lore of player's held item to "&6Reload Time: &c""" + reload +"""ms"
					set line 3 of lore of player's held item to "&6Damage: &c""" + damage +""""
					set line 4 of lore of player's held item to "&6Ammunition: &c""" + ammo + """"
					loop """ + str(int(reload)/100) +""" times:
						console command "/execute at %player% run playsound minecraft:block.iron_door.open master @a ~ ~ ~ 0.5 2"
						wait 0.1 second	

					set {ammo.%{_id}%} to amount of """ + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """" in player's inventory
					if {ammo.%{_id}%} > """ + capacity + """:
						remove """ + capacity + """ """ + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """" from player's inventory
						set {""" + tag + """.%{_id}%} to """ + capacity + """
					else:
						
						remove """ + capacity + """ """ + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """" from player's inventory
						set {""" + tag + """.%{_id}%} to {ammo.%{_id}%}
						
					edit bossbar "%player%" title to "&6""" + name + """: &c%{""" + tag + """.%line 5 of lore of player's held item%}%"
					set bossbar "%player%" value to {""" + tag + """.%line 5 of lore of player's held item%} * """ + str(100/int(capacity)) + """
				else:
					send action bar "&6You are missing &c""" + ammo + """&6!" to player

        set slot 10 of {_store} to leather horse armor named "<##""" + colour + """>Glock-19" with nbt "{display:{color:""" + colour2 + """},HideFlags:127}"
        set line 1 of lore of slot 10 of {_store} to "&6Cartridge: &c""" + capacity + """&6/&c""" + capacity + """"
        set line 2 of lore of slot 10 of {_store} to "&6Reload Time: &c""" + reload + """ms"
        set line 3 of lore of slot 10 of {_store} to "&6Damage: &c""" + damage + """"
        set line 4 of lore of slot 10 of {_store} to "&6Ammunition: &c""" + ammo +""""
        set line 6 of lore of slot 10 of {_store} to "&6Type: &c""" + type +""""
        set line 7 of lore of slot 10 of {_store} to "&6Cost: &c""" + cost + """"                    

                give player leather horse armor named "<##""" + colour + """>""" + name + """" with nbt "{display:{color:""" + colour2 + """},HideFlags:127}"
            
        
        if projectile has scoreboard tag \"""" + capstag + """":
            set {_dmg} to """ + damage + """ - {_armour} / 2    

    set {""" + tag + """cd.%player%} to now
        set {""" + tag + """cd.%loop-player%} to now

        set slot 10 of {_store} to leather horse armor named "<##""" + colour + """>""" + name + """ &6[&cx1&6]" with nbt "{display:{color:""" + colour2 + """},HideFlags:127}"
        set line 1 of lore of slot 10 of {_store} to "&6Cartridge: &c""" + capacity + """&6/&c""" + capacity + """"
        set line 2 of lore of slot 10 of {_store} to "&6Reload Time: &c""" + reload + """ms"
        set line 3 of lore of slot 10 of {_store} to "&6Damage: &c""" + damage + """"
        set line 4 of lore of slot 10 of {_store} to "&6Ammunition: &c""" + ammo + """"
        set line 6 of lore of slot 10 of {_store} to "&6Cost: &c""" + cost + """"

        set slot 10 of {_store} to """ + capacity + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """ &6[&cx""" + capacity + """&6]"
        set line 2 of lore of slot 10 of {_store} to "&6Cost: &c""" + capacity + """"        

on inventory click:
    if name of event-item is "<##""" + colour + """>""" + name + """ &6[&cx1&6]":
        if player doesn't have enough space for bedrock:
            close player's inventory
            console command "/execute at %player% run playsound minecraft:entity.enderman.teleport master %player% ~ ~ ~ 10000 0"  
            send "&7Gun&4PVP&aMC&6: Your inventory is full!"
            stop        
        if {coins::%player's uuid%} > """ + str(int(cost)-1) + """:
            set {coins::%player's uuid%} to {coins::%player's uuid%} - """ + cost + """
            console command "/execute at %player% run playsound block.note_block.pling master %player% ~ ~ ~ 100000 2"
            give player leather horse armor named "<##""" + colour + """>""" + name + """" with nbt "{display:{color:""" + colour2 + """},HideFlags:127}"
            send "&6[&cGunner&6] Mike: Pleasure doin' business with ya"
        else:
            send "&6[&cGunner&6] Mike: Ya can't afford that mate"
            console command "/execute at %player% run playsound minecraft:entity.enderman.teleport master %player% ~ ~ ~ 10000 0"

on inventory click:
    if name of event-item is "<##""" + ammocolour + """>""" + ammo + """ &6[&cx""" + capacity + """&6]":
        if player doesn't have enough space for bedrock:
            close player's inventory
            console command "/execute at %player% run playsound minecraft:entity.enderman.teleport master %player% ~ ~ ~ 10000 0"  
            send "&7Gun&4PVP&aMC&6: Your inventory is full!"
            stop        
        if {coins::%player's uuid%} > """ + str(int(capacity)-1) + """:
            set {coins::%player's uuid%} to {coins::%player's uuid%} - """ + capacity + """
            console command "/execute at %player% run playsound block.note_block.pling master %player% ~ ~ ~ 100000 2"
            give player """ + capacity + ammotype + """ named "<##""" + ammocolour + """>""" + ammo + """"
            send "&6[&cGunner&6] Mike: Pleasure doin' business with ya"
        else:
            send "&6[&cGunner&6] Mike: Ya can't afford that mate"
            console command "/execute at %player% run playsound minecraft:entity.enderman.teleport master %player% ~ ~ ~ 10000 0"
            

""")