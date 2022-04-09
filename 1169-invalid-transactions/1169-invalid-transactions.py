class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        r, inv = {}, []
		
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            transactions[i] = (name, time, amount, city)
            time = int(time)

            if time not in r:
                r[time] = {name: {city}}
            else:
                if name not in r[time]:
                    r[time][name]={city}
                else:
                    r[time][name].add(city)


        for i, t in enumerate(transactions):
            name, time, amount, city = t

            if float(amount) > 1000:
                inv.append(','.join(t))
                continue

            time = int(time)
            for j in range(time-60, time+61):
                if j not in r:            continue
                if name not in r[j]:      continue

                if len(r[j][name]) > 1 or (r[j][name] != {city}):
                    inv.append(','.join(t))
                    break

        return inv