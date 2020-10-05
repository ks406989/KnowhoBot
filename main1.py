       

        

            rs6
            
            data = {

                "Eyecon Name": frbseyename,

                "Mob": num,

                "Truecaller name": frbsetrname,

                "Facebook": frbsefb,

                "Mail": frbsetrmail

            }

            firebase.put('/knowho-log', num, data)

        elif frbseyename and frbsefb and frbsetrname:

            data = {

                "Eyecon Name": frbseyename,

                "Mob": num,

                "Truecaller name": frbsetrname,

                "

                "Eyecon Name": frbseyename,

                "Mob": num,

                "Truecaller name": frbsetrname

            }

            firebase.put('/knowho-log', num, data)

        elif frbsetrname and frbsetrmail:

            data = {

                "Truecaller name": frbsetrname,

                "Mob": num,

                "Mail": frbsetrmail

            }

            firebase.put('/knowho-log', num, data)

        elif frbsetrname:

            data = {

                "Truecaller name": frbsetrname

            }

            firebase.put('/knowho-log', num, data)

    else:

        pro.edit("`Only` **10** `digit numbers allowed` 🤦🏻‍♂️")

app.run()




