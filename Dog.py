class Dog:
    def __init__(self, *kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
    # def __init__(self, name: str, parents: set, size: str,
    #              height: str, weight: str, lifespan: str,
    #              touchiness: str, barking: str, activity: str,
    #              traits: str, hypoallergenic: str, imgs: set):
    #     self.name = name
    #     self.parents = parents
    #     self.size = size
    #     self.height = height
    #     self.weight = weight
    #     self.lifespan = lifespan
    #     self.touchiness = touchiness
    #     self.barking = barking
    #     self.activity = activity
    #     self.traits = traits
    #     self.hypoallergenic = hypoallergenic
    #     self.imgs = imgs

    def __str__(self):
        return f'{self.name}, the result of mixing {" and ".join(self.parents)}'

    def __repr__(self):
        return str([self.name, self.parents, self.size, self.height, self.weight, self.lifespan, self.touchiness,
                self.barking, self.activity, self.traits, self.hypoallergenic, self.imgs])
