def save_file():
    """This method saves the data to a mission file"""
    #TODO: Expand this to save every part of the mission file:
    #   - Comments/Copyright
    #   - Mission
    #   - Events
    logging.debug("Saving selected file...")
    compile_mission()

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    for item in config.mission_file_items.items_list:
        f.write(item.to_string())
        f.write("\n\n\n")       # add whitespace between missions, per the Creating Missions guidelines
    f.close()

    logging.debug("Done.")
# end save_file 