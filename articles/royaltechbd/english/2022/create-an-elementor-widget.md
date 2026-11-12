---
archive_id: royaltechbd-2044
source: royaltechbd
source_name: Royal Technologies
wordpress_id: 2044
title: Create an Elementor Widget
slug: create-an-elementor-widget
language: en
status: publish
published_at: '2022-03-11T00:14:58'
published_at_gmt: '2022-03-10T18:14:58'
modified_at: '2026-09-28T09:03:23'
modified_at_gmt: '2026-09-28T03:03:23'
original_url: https://www.royaltechbd.com/create-an-elementor-widget/
author: Mehdi Akram
categories:
- Web Development
- Wordpress
tags: []
content_hash: daf6d81e43a3b5a8aed626c09fac10101f56695ddde52ce33af0084da6bf7323
archived_at: '2026-11-12T08:31:02.640785+00:00'
---

### [Step 1. Setup the plugin.](https://www.benmarshall.me/create-an-elementor-widget/#step-1)

To begin let’s start with setting up the *Awesomesauce* custom plugin:

1. Create a directory called `elementor-awesomesauce` in `wp-content/plugins`
2. In the plugin directory, create the following files & directories:
   - `elementor-awesomesauce.php` – defines the plugin
   - `class-elementor-awesomesauce.php` – verifies requirements
   - `class-widgets.php` – registers the plugin’s custom widgets & scripts
   - `widgets/class-awesomesauce.php` – the custom *Awesomesauce Elementor* widget
   - `assets/js/awesomesauce.js` – some JS for the custom widget
   - `assets/css/awesomesauce.css` – some CSS for the custom widget

### [Step 2. Define the plugin.](https://www.benmarshall.me/create-an-elementor-widget/#step-2)

In the `elementor-awesomesauce.php` file, we’ll define the plugin so WordPress recognizes and allows you to enable in the admin dashboard.

`elementor-awesomesauce.php`

```
<?php
/**
 * Elementor Awesomesauce WordPress Plugin
 *
 * @package ElementorAwesomesauce
 *
 * Plugin Name: Elementor Awesomesauce
 * Description: Simple Elementor plugin example
 * Plugin URI:  https://www.benmarshall.me/build-custom-elementor-widgets/
 * Version:     1.0.0
 * Author:      Ben Marshall
 * Author URI:  https://www.benmarshall.me
 * Text Domain: elementor-awesomesauce
 */
define( 'ELEMENTOR_AWESOMESAUCE', __FILE__ );
/**
 * Include the Elementor_Awesomesauce class.
 */
require plugin_dir_path( ELEMENTOR_AWESOMESAUCE ) . 'class-elementor-awesomesauce.php';
```

### [Step 3. Initialize the plugin.](https://www.benmarshall.me/create-an-elementor-widget/#step-3)

In the `class-elementor-awesomesauce.php` file, we’ll initialize the plugin and verify the PHP, WordPress, and Elementor version requirements are met.

```
<?php
/**
 * Elementor_Awesomesauce class.
 *
 * @category   Class
 * @package    ElementorAwesomesauce
 * @subpackage WordPress
 * @author     Ben Marshall <me@benmarshall.me>
 * @copyright  2020 Ben Marshall
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://www.benmarshall.me/build-custom-elementor-widgets/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 7.3.9
 */
if ( ! defined( 'ABSPATH' ) ) {
	// Exit if accessed directly.
	exit;
}
/**
 * Main Elementor Awesomesauce Class
 *
 * The init class that runs the Elementor Awesomesauce plugin.
 * Intended To make sure that the plugin's minimum requirements are met.
 *
 * You should only modify the constants to match your plugin's needs.
 *
 * Any custom code should go inside Plugin Class in the class-widgets.php file.
 */
final class Elementor_Awesomesauce {
	/**
	 * Plugin Version
	 *
	 * @since 1.0.0
	 * @var string The plugin version.
	 */
	const VERSION = '1.0.0';
	/**
	 * Minimum Elementor Version
	 *
	 * @since 1.0.0
	 * @var string Minimum Elementor version required to run the plugin.
	 */
	const MINIMUM_ELEMENTOR_VERSION = '2.0.0';
	/**
	 * Minimum PHP Version
	 *
	 * @since 1.0.0
	 * @var string Minimum PHP version required to run the plugin.
	 */
	const MINIMUM_PHP_VERSION = '7.0';
	/**
	 * Constructor
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function __construct() {
		// Load the translation.
		add_action( 'init', array( $this, 'i18n' ) );
		// Initialize the plugin.
		add_action( 'plugins_loaded', array( $this, 'init' ) );
	}
	/**
	 * Load Textdomain
	 *
	 * Load plugin localization files.
	 * Fired by `init` action hook.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function i18n() {
		load_plugin_textdomain( 'elementor-awesomesauce' );
	}
	/**
	 * Initialize the plugin
	 *
	 * Validates that Elementor is already loaded.
	 * Checks for basic plugin requirements, if one check fail don't continue,
	 * if all check have passed include the plugin class.
	 *
	 * Fired by `plugins_loaded` action hook.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function init() {
		// Check if Elementor installed and activated.
		if ( ! did_action( 'elementor/loaded' ) ) {
			add_action( 'admin_notices', array( $this, 'admin_notice_missing_main_plugin' ) );
			return;
		}
		// Check for required Elementor version.
		if ( ! version_compare( ELEMENTOR_VERSION, self::MINIMUM_ELEMENTOR_VERSION, '>=' ) ) {
			add_action( 'admin_notices', array( $this, 'admin_notice_minimum_elementor_version' ) );
			return;
		}
		// Check for required PHP version.
		if ( version_compare( PHP_VERSION, self::MINIMUM_PHP_VERSION, '<' ) ) {
			add_action( 'admin_notices', array( $this, 'admin_notice_minimum_php_version' ) );
			return;
		}
		// Once we get here, We have passed all validation checks so we can safely include our widgets.
		require_once 'class-widgets.php';
	}
	/**
	 * Admin notice
	 *
	 * Warning when the site doesn't have Elementor installed or activated.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function admin_notice_missing_main_plugin() {
		deactivate_plugins( plugin_basename( ELEMENTOR_AWESOMESAUCE ) );
		return sprintf(
			wp_kses(
				'<div class="notice notice-warning is-dismissible"><p><strong>"%1$s"</strong> requires <strong>"%2$s"</strong> to be installed and activated.</p></div>',
				array(
					'div' => array(
						'class'  => array(),
						'p'      => array(),
						'strong' => array(),
					),
				)
			),
			'Elementor Awesomesauce',
			'Elementor'
		);
	}
	/**
	 * Admin notice
	 *
	 * Warning when the site doesn't have a minimum required Elementor version.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function admin_notice_minimum_elementor_version() {
		deactivate_plugins( plugin_basename( ELEMENTOR_AWESOMESAUCE ) );
		return sprintf(
			wp_kses(
				'<div class="notice notice-warning is-dismissible"><p><strong>"%1$s"</strong> requires <strong>"%2$s"</strong> version %3$s or greater.</p></div>',
				array(
					'div' => array(
						'class'  => array(),
						'p'      => array(),
						'strong' => array(),
					),
				)
			),
			'Elementor Awesomesauce',
			'Elementor',
			self::MINIMUM_ELEMENTOR_VERSION
		);
	}
	/**
	 * Admin notice
	 *
	 * Warning when the site doesn't have a minimum required PHP version.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function admin_notice_minimum_php_version() {
		deactivate_plugins( plugin_basename( ELEMENTOR_AWESOMESAUCE ) );
		return sprintf(
			wp_kses(
				'<div class="notice notice-warning is-dismissible"><p><strong>"%1$s"</strong> requires <strong>"%2$s"</strong> version %3$s or greater.</p></div>',
				array(
					'div' => array(
						'class'  => array(),
						'p'      => array(),
						'strong' => array(),
					),
				)
			),
			'Elementor Awesomesauce',
			'Elementor',
			self::MINIMUM_ELEMENTOR_VERSION
		);
	}
}
// Instantiate Elementor_Awesomesauce.
new Elementor_Awesomesauce();
```

### [Step 4. Build the custom widget.](https://www.benmarshall.me/create-an-elementor-widget/#step-5)

In the `widgets/class-awesomesauce.php` file, we’ll build the custom Elementor widget, *Awesomesauce*.

`widgets/class-awesomesauce.php`

```
<?php
/**
 * Awesomesauce class.
 *
 * @category   Class
 * @package    ElementorAwesomesauce
 * @subpackage WordPress
 * @author     Ben Marshall <me@benmarshall.me>
 * @copyright  2020 Ben Marshall
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://www.benmarshall.me/build-custom-elementor-widgets/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 7.3.9
 */
namespace ElementorAwesomesauce\Widgets;
use Elementor\Widget_Base;
use Elementor\Controls_Manager;
// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();
/**
 * Awesomesauce widget class.
 *
 * @since 1.0.0
 */
class Awesomesauce extends Widget_Base {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'awesomesauce', plugins_url( '/assets/css/awesomesauce.css', ELEMENTOR_AWESOMESAUCE ), array(), '1.0.0' );
	}
	/**
	 * Retrieve the widget name.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'awesomesauce';
	}
	/**
	 * Retrieve the widget title.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return __( 'Awesomesauce', 'elementor-awesomesauce' );
	}
	/**
	 * Retrieve the widget icon.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'fa fa-pencil';
	}
	/**
	 * Retrieve the list of categories the widget belongs to.
	 *
	 * Used to determine where to display the widget in the editor.
	 *
	 * Note that currently Elementor supports only one category.
	 * When multiple categories passed, Elementor uses the first one.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return array( 'general' );
	}
	
	/**
	 * Enqueue styles.
	 */
	public function get_style_depends() {
		return array( 'awesomesauce' );
	}
	/**
	 * Register the widget controls.
	 *
	 * Adds different input fields to allow the user to change and customize the widget settings.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _register_controls() {
		$this->start_controls_section(
			'section_content',
			array(
				'label' => __( 'Content', 'elementor-awesomesauce' ),
			)
		);
		$this->add_control(
			'title',
			array(
				'label'   => __( 'Title', 'elementor-awesomesauce' ),
				'type'    => Controls_Manager::TEXT,
				'default' => __( 'Title', 'elementor-awesomesauce' ),
			)
		);
		$this->add_control(
			'description',
			array(
				'label'   => __( 'Description', 'elementor-awesomesauce' ),
				'type'    => Controls_Manager::TEXTAREA,
				'default' => __( 'Description', 'elementor-awesomesauce' ),
			)
		);
		$this->add_control(
			'content',
			array(
				'label'   => __( 'Content', 'elementor-awesomesauce' ),
				'type'    => Controls_Manager::WYSIWYG,
				'default' => __( 'Content', 'elementor-awesomesauce' ),
			)
		);
		$this->end_controls_section();
	}
	/**
	 * Render the widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function render() {
		$settings = $this->get_settings_for_display();
		$this->add_inline_editing_attributes( 'title', 'none' );
		$this->add_inline_editing_attributes( 'description', 'basic' );
		$this->add_inline_editing_attributes( 'content', 'advanced' );
		?>
		<h2 <?php echo $this->get_render_attribute_string( 'title' ); ?><?php echo wp_kses( $settings['title'], array() ); ?></h2>
		<div <?php echo $this->get_render_attribute_string( 'description' ); ?><?php echo wp_kses( $settings['description'], array() ); ?></div>
		<div <?php echo $this->get_render_attribute_string( 'content' ); ?><?php echo wp_kses( $settings['content'], array() ); ?></div>
		<?php
	}
	/**
	 * Render the widget output in the editor.
	 *
	 * Written as a Backbone JavaScript template and used to generate the live preview.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _content_template() {
		?>
		<#
		view.addInlineEditingAttributes( 'title', 'none' );
		view.addInlineEditingAttributes( 'description', 'basic' );
		view.addInlineEditingAttributes( 'content', 'advanced' );
		#>
		<h2 {{{ view.getRenderAttributeString( 'title' ) }}}>{{{ settings.title }}}</h2>
		<div {{{ view.getRenderAttributeString( 'description' ) }}}>{{{ settings.description }}}</div>
		<div {{{ view.getRenderAttributeString( 'content' ) }}}>{{{ settings.content }}}</div>
		<?php
	}
}
```

#### [Register the widgets & scripts.](https://www.benmarshall.me/create-an-elementor-widget/#step-4)

Each Elementor widget can have it’s own CSS & JS files that’ll be loaded conditionally if it appears on the page. This is an important aspect of the component-based approach that helps boost site performance so only the resources needed are loaded.

In our example widget, we’ve registered all styles and scripts in the widget’s class constructor:

`class-awesomesauce.php`

```
/**
 * Class constructor.
 *
 * @param array $data Widget data.
 * @param array $args Widget arguments.
 */
public function __construct( $data = array(), $args = null ) {
	parent::__construct( $data, $args );
	wp_register_style( 'awesomesauce', plugins_url( '/assets/css/accordion.css', ELEMENTOR_AWESOMESAUCE ), array(), '1.0.0' );
}
```

## [Available widget field options.](https://www.benmarshall.me/create-an-elementor-widget/#field-options)

Elementor is super powerful allowing you to easily add custom tabs, fields, style setting and even responsiveness. In the code above, the `_register_controls` is where we’ve already added a few fields for *title, description and content*, but what if you need more? Check out the examples below to add even more awesomeness to your *Elementor Awesomesauce* plugin.

### [Add Elementor Widget Tabs](https://www.benmarshall.me/create-an-elementor-widget/#widget-tabs)

Elementor widgets can have configurable tabbed sections. For instance, many core widgets in Elementor include *Content*, *Style* & *Advanced* tabs. The tabbed sections allow you to add customizable fields and other content specific to each widget instance on a page.

#### Creating a Widget Content Tab

`widgets/awesomesauce.php` – In the `_register_controls` method.

```
$this->start_controls_section(
  'section_content',
  [
    'label' => __( 'Content', 'elementor-awesomesauce' ),
  ]
);
/* Add the options you'd like to show in this tab here */
$this->end_controls_section();
```

#### Creating a Widget Style Tab

`widgets/awesomesauce.php` – In the `_register_controls` method.

```
$this->start_controls_section(
  'style_section',
  [
    'label' => __( 'Style Section', 'elementor-awesomesauce' ),
    'tab' => \Elementor\Controls_Manager::TAB_STYLE,
  ]
);
/* Add the options you'd like to show in this tab here */
$this->end_controls_section();
```

### [Elementor Widget Image Field](https://www.benmarshall.me/create-an-elementor-widget/#image-field)

The ability to add/change images is crucial to any good WordPress theme, here’s how to add a custom image field in an Elementor widget with `Controls_Manager::MEDIA`:

widgets/awesomesauce.php – In the `_register_controls` method.

```
$this->add_control(
			'mask_image',
			[
				'label' => __( 'Mask Image', 'elementor-awesomesauce' ),
				'type' => Controls_Manager::MEDIA,
        'default' => [
					'url' => Utils::get_placeholder_image_src(),
				]
			]
		);
```

### [Elementor Widget Select Dropdown](https://www.benmarshall.me/create-an-elementor-widget/#dropdown)

What if we wanted to allow the user to select the HTML element for the title, it’s also a cinch with `Controls_Manager::SELECT`:

```
$this->add_control(
	'border_style',
	array
		'label'   => __( 'Border Style', 'plugin-domain' ),
		'type'    => \Elementor\Controls_Manager::SELECT,
		'default' => 'solid',
		'options' => array(
			'solid'  => __( 'Solid', 'plugin-domain' ),
			'dashed' => __( 'Dashed', 'plugin-domain' ),
			'dotted' => __( 'Dotted', 'plugin-domain' ),
			'double' => __( 'Double', 'plugin-domain' ),
			'none'   => __( 'None', 'plugin-domain' ),
		),
	)
);
```

Next you’ll need to render the select output with the `render` method:

```
protected function render() {
  $settings = $this->get_settings_for_display();
  echo '&lt;div style="border-style: ' . esc_attr( $settings['border_style'] ) . '"> .. &lt;/div>';
}
```

Lastly, you’ll want to create the template Elementor uses when in the editor mode in the `_content_template` method:

```
protected function _content_template() {
	?>
	&lt;div style="border-style: {{ settings.border_style }}"> .. &lt;/div>
	&lt;?php
}
```

### [Elementor Widget Button Group](https://www.benmarshall.me/create-an-elementor-widget/#buttongroup)

How about adding alignment options using a button group, easy with `Controls_Manager::CHOOSE`:

`widgets/awesomesauce.php` – In the `_register_controls` method.

```
$this->add_control(
  'text_align',
  [
    'label' => __( 'Alignment', 'elementor-awesomesauce' ),
    'type' => \Elementor\Controls_Manager::CHOOSE,
    'options' => [
      'left' => [
        'title' => __( 'Left', 'elementor-awesomesauce' ),
        'icon' => 'fa fa-align-left',
      ],
      'center' => [
        'title' => __( 'Center', 'elementor-awesomesauce' ),
        'icon' => 'fa fa-align-center',
      ],
      'right' => [
        'title' => __( 'Right', 'elementor-awesomesauce' ),
        'icon' => 'fa fa-align-right',
      ],
    ],
    'default' => 'center',
    'toggle' => true,
  ]
);
```

#### [Elementor Widget Typography Options](https://www.benmarshall.me/create-an-elementor-widget/#typography)

Elementor comes with a powerful typography editor that includes responsive options, here’s how you add it with `Group_Control_Typography` & `Scheme_Typography::TYPOGRAPHY_1`.

`widgets/awesomesauce.php` – At the top of the file where the `use` statements are located.

```
use Elementor\Group_Control_Typography;
use Elementor\Scheme_Typography;
```

`widgets/awesomesauce.php` – In the `_register_controls` method.

```
$this->add_group_control(
  Group_Control_Typography::get_type(),
  [
    'name'     => 'content_typography',
    'label'    => __( 'Typography', 'elementor-awesomesauce' ),
    'scheme'   => Scheme_Typography::TYPOGRAPHY_1,
    'selector' => '{{WRAPPER}} .elementor-awesomesauce',
    'fields_options' => [
      'letter_spacing' => [
        'range' => [
          'min' => 0,
          'max' => 100
        ]
      ]
    ]
  ]
);
```

### [Adding a Elementor Repeater Control](https://www.benmarshall.me/create-an-elementor-widget/#repeater)

Elementor repeater control allows you to build repeatable blocks of fields.

You can create, for example, a set of fields that will contain a title and a WYSIWYG text – the user will then be able to add “rows”, and each row will contain a title and a text. The data can be wrapper in custom HTML tags, designed using CSS, and interact using JS or external libraries.

The control is defined in **[Control\_Repeater](https://code.elementor.com/classes/elementor-control_repeater/)** class which extends **[Base\_Data\_Control](https://code.elementor.com/classes/elementor-base_data_control/)** class.

Note that when using the control, the type should be set using the `\Elementor\Controls_Manager::REPEATER` constant.

##### Example Repeater Control Usage

Add the following code in the `widgets/awesomesauce.php` file where all Elementor widget controls are defined:

```
<?php
namespace ElementorAwesomesauce\Widgets;
 
use Elementor\Widget_Base;
use Elementor\Controls_Manager;
 
if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly
class Elementor_Widget_Test extends \Elementor\Widget_Base {
	public function get_name() {
		return 'awesomesauce';
	}
	public function get_title() {
		return __( 'Awesomesauce', 'elementor-awesomesauce' );
  }
  
  public function get_icon() {
    return 'fa fa-pencil';
  }
  public function get_categories() {
    return [ 'general' ];
  }
	protected function _register_controls() {
		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Content', 'elementor-awesomesauce' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);
		$repeater = new \Elementor\Repeater();
		$repeater->add_control(
			'list_title', [
				'label' => __( 'Title', 'elementor-awesomesauce' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => __( 'List Title' , 'elementor-awesomesauce' ),
				'label_block' => true,
			]
		);
		$repeater->add_control(
			'list_content', [
				'label' => __( 'Content', 'elementor-awesomesauce' ),
				'type' => \Elementor\Controls_Manager::WYSIWYG,
				'default' => __( 'List Content' , 'elementor-awesomesauce' ),
				'show_label' => false,
			]
		);
		$repeater->add_control(
			'list_color',
			[
				'label' => __( 'Color', 'elementor-awesomesauce' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} {{CURRENT_ITEM}}' => 'color: {{VALUE}}'
				],
			]
		);
		$this->add_control(
			'list',
			[
				'label' => __( 'Repeater List', 'elementor-awesomesauce' ),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => $repeater->get_controls(),
				'default' => [
					[
						'list_title' => __( 'Title #1', 'elementor-awesomesauce' ),
						'list_content' => __( 'Item content. Click the edit button to change this text.', 'elementor-awesomesauce' ),
					],
					[
						'list_title' => __( 'Title #2', 'elementor-awesomesauce' ),
						'list_content' => __( 'Item content. Click the edit button to change this text.', 'elementor-awesomesauce' ),
					],
				],
				'title_field' => '{{{ list_title }}}',
			]
		);
		$this->end_controls_section();
	}
	protected function render() {
		$settings = $this->get_settings_for_display();
		if ( $settings['list'] ) {
			echo '<dl>';
			foreach (  $settings['list'] as $item ) {
				echo '<dt class="elementor-repeater-item-' . $item['_id'] . '">' . $item['list_title'] . '</dt>';
				echo '<dd>' . $item['list_content'] . '</dd>';
			}
			echo '</dl>';
		}
	}
	protected function _content_template() {
		?>
		<# if ( settings.list.length ) { #>
		<dl>
			<# _.each( settings.list, function( item ) { #>
				<dt class="elementor-repeater-item-{{ item._id }}">{{{ item.list_title }}}</dt>
				<dd>{{{ item.list_content }}}</dd>
			<# }); #>
			</dl>
		<# } #>
		<?php
	}
}
```

### [Complete List of Available Elementor Fields](https://www.benmarshall.me/create-an-elementor-widget/#all-fields)

Here’s a list of all available [Elementor field controls](https://developers.elementor.com/elementor-controls/):

- [Text](https://developers.elementor.com/elementor-controls/text-control/) — A simple text field.
- [Number](https://developers.elementor.com/number-control/) — A simple number field.
- [Textarea](https://developers.elementor.com/elementor-controls/textarea-control/) — A textarea field.
- [WYSIWYG](https://developers.elementor.com/elementor-controls/wysiwyg-control/) — The WordPress rich-text editor (TinyMCE).
- [Code](https://developers.elementor.com/elementor-controls/code-control/) — A code editor textarea based on Ace editor.
- [Hidden](https://developers.elementor.com/elementor-controls/hidden-control/) — A hidden input field in the panel, to save data in the database without an input field in the panel.
- [Switcher](https://developers.elementor.com/elementor-controls/switcher-control/) — A switcher control (on/off), a fancy representation of checkbox.
- [Popover Toggle](https://developers.elementor.com/elementor-controls/popover-toggle-control/) — A toggle button to open and close a popover.
- [Select](https://developers.elementor.com/elementor-controls/select-control/) — A simple select box field.
- [Select2](https://developers.elementor.com/elementor-controls/select2-control/) — A select box field based on the Select2 plugin.
- [Choose](https://developers.elementor.com/elementor-controls/choose-control/) — A radio buttons styled as groups of buttons with icons.
- [Color](https://developers.elementor.com/elementor-controls/color-control/) — A color picker field with an alpha slider.
- [Font](https://developers.elementor.com/elementor-controls/font-control/) — A font select box field based on Google Fonts library.
- [Date-Time](https://developers.elementor.com/elementor-controls/date-time-control/) — A date/time picker field based on the Flatpickr library.
- [Entrance Animation](https://developers.elementor.com/elementor-controls/entrance-animation-control/) — An entrance animation select box field based on Animate.css library.
- [Hover Animation](https://developers.elementor.com/elementor-controls/hover-animation-control/) — A hover animation select box field based on Hover.css library.
- [Gallery](https://developers.elementor.com/elementor-controls/gallery-control/) — A gallery field based on the WordPress media library.
- [Repeater](https://developers.elementor.com/elementor-controls/repeater-control/) — Repeater controls allow you to build repeatable blocks of fields.

## [Adding Elementor Widget CSS & JS](https://www.benmarshall.me/create-an-elementor-widget/#elementor-scripts)

Building sites with a component-based approach like Elementor widgets provides allows you to load JS & CSS scripts only when the widget is used on the page. This gives you a nice boost in performance since your pages are only loading what’s needed.

You accomplish this by first registering all of your JS & CSS files in the `class-widgets.php` file using the `widget_scripts` method:

```
public function widget_scripts() {
  wp_register_style( 'elementor-awesomesauce', plugins_url( '/assets/css/elementor-awesomesauce.css', __FILE__ ), [], '1.0.0' );
}
```

Next, you’ll need to enqueue the script when the widget appears on the page in the `widgets/awesomesauce.php` file using the [`get_style_depends`](https://code.elementor.com/methods/elementor-element_base-get_style_depends/) and [`get_script_depends`](https://code.elementor.com/methods/elementor-element_base-get_script_depends/) methods:

```
public function get_style_depends() {
  $styles = [ 'elementor-awesomesauce' ];
  return $styles;
}
public function get_script_depends() {
  $scripts = [];
  return $scripts;
}
```

Now your JS & CSS files will only load when needed… awesome sauce!

## [Create Conditional Fields/Controls](https://www.benmarshall.me/create-an-elementor-widget/#conditional-fields)

What about conditional fields? Elementor can handle that too. It’s as easy as using the `condition` argument when creating a control:

```
'condition' => array(
  'fieldkey' => 'value',
),
```

For more information on conditional fields and more advanced usage, see the [Conditional Elementor Controls](https://www.benmarshall.me/conditional-elementor-controls/) post.

## [Create Custom Dynamic Field/Tag Values](https://www.benmarshall.me/create-an-elementor-widget/#dynamic-tags)

A common need and important aspect of most forms it the ability to add dynamic content to the field values. Whether that’s to pre populated a user’s email address, add a hidden field with URL parameters, pass the post excerpt, post content, author info, archive title, site name, site logo or more.

### Create a Custom Dynamic Tag

Start by creating a class that extends the `Elementor\Core\DynamicTags\Tag` class and fill in all the required methods. Each Dynamic Tag needs to have a few basic settings like a unique name, a title that will be used. On top of that, we have some advanced settings like the Dynamic Tag controls which are basically optional fields where the user can configure his custom data. And a render method that generates the final output based on the user settings from the Dynamic Tag’s controls.

### Create the Dynamic Tag Structure

As mentioned above, Elementor Dynamic Tag extends the `Elementor\Core\DynamicTags\Tag` class and inherits its methods. A simple Dynamic Tag skeleton will look like this:

```
Class Elementor_Test_Tag extends \Elementor\Core\DynamicTags\Tag {
	public function get_name() {}
	public function get_title() {}
	public function get_group() {}
	public function get_categories() {}
	protected function _register_controls() {}
	public function render() {}
}
```

Let’s break it down:

- `get_name()` – Returns a Tag name (id) that will be used in the code.
- `get_title()` – The Tag title that will be displayed as the Tag label.
- `get_group()` – Return which group the Tag will appear under. (tag groups will be explained later on).
- `get_categories()` – Return the control categories the Tag belongs to. (tag categories will be explained later on).
- `_register_controls()` – (Optional) Define Tag controls (setting fields).
- `render()` – The Tag output.

The `Elementor\Core\DynamicTags\Tag` class has many more methods you can use to do different things, but for now, this should be good enough.

### Example of a Simple Dynamic Tag

To put all of the pieces together we are going to create a simple Elementor Dynamic Tag which will return a server variable.

##### Dynamic Tag Class

First, we need to create a class that extends the `Elementor\Core\DynamicTags\Tag` class:

```
Class Elementor_Server_Var_Tag extends \Elementor\Core\DynamicTags\Tag {
}
```

##### Dynamic Tag Settings

Now that we have a class for our dynamic tag, we can start filling in the methods, and we start with the simple ones:

```
Class Elementor_Server_Var_Tag extends \Elementor\Core\DynamicTags\Tag {
	public function get_name() {
		return 'server-variable';
	}
	public function get_title() {
		return __( 'Server Variable', 'elementor' );
	}
	public function get_group() {
		return 'request-variables';
	}
	public function get_categories() {
		return [ \Elementor\Modules\DynamicTags\Module::TEXT_CATEGORY ];
	}
}
```

**Side Note:** By default, Elementor comes with these dynamic tag categories:

- `TEXT_CATEGORY` – Dynamic tags text controls.
- `URL_CATEGORY` – Dynamic tags URL controls.
- `IMAGE_CATEGORY` – Dynamic tags image controls.
- `MEDIA_CATEGORY` – Dynamic tags media controls.
- `POST_META_CATEGORY` – Dynamic tags post meta controls.
- `GALLERY_CATEGORY` – Dynamic tags gallery controls.

##### Dynamic Tag Controls

Next, we need to add the Dynamic Tag controls using the `_register_controls()` method:

```
Class Elementor_Server_Var_Tag extends \Elementor\Core\DynamicTags\Tag {
	protected function _register_controls() {
		$variables = [];
		foreach ( array_keys( $_SERVER ) as $variable ) {
			$variables[ $variable ] = ucwords( str_replace( '_', ' ', $variable ) );
     		}
		$this->add_control(
			'param_name',
			[
				'label'   => __( 'Param Name', 'elementor' ),
			        'type' => \Elementor\Controls_Manager::SELECT,
			        'options' => $variables,
			]
		);
	}
}
```

We add a single select control with the list of the sever variables to choose from. Note that this is just an example, and in a real-world use case you would probably want to exclude some of the server variables.

##### Dynamic Tag Value

Last, we need to implement the `render()` method, which takes the variable name the user selected in the control and returns the server corresponding variable value:

```
Class Elementor_Server_Var_Tag extends \Elementor\Core\DynamicTags\Tag {
	public function render() {
		$param_name = $this->get_settings( 'param_name' );
		if ( ! $param_name ) {
			return;
		}
		if ( ! isset( $_SERVER[ $param_name ] ) ) {
			return;
		}
		$value = $_SERVER[ $param_name ];
		echo wp_kses_post( $value );
	}
}
```

The `render()` method simply checks that a server variable with the selected param name exists and echo it to the buffer after some minimal escaping.

##### The Entire Code

Altogether the Dynamic tag class with some extra phpDocs should look something like this:

```
<?php
Class Elementor_Server_Var_Tag extends \Elementor\Core\DynamicTags\Tag {
	/**
	* Get Name
	*
	* Returns the Name of the tag
	*
	* @since 2.0.0
	* @access public
	*
	* @return string
	*/
	public function get_name() {
		return 'server-variable';
	}
	/**
	* Get Title
	*
	* Returns the title of the Tag
	*
	* @since 2.0.0
	* @access public
	*
	* @return string
	*/
	public function get_title() {
		return __( 'Server Variable', 'elementor-pro' );
	}
   
	/**
	* Get Group
	*
	* Returns the Group of the tag
	*
	* @since 2.0.0
	* @access public
	*
	* @return string
	*/
	public function get_group() {
		return 'request-variables';
	}
	/**
	* Get Categories
	*
	* Returns an array of tag categories
	*
	* @since 2.0.0
	* @access public
	*
	* @return array
	*/
	public function get_categories() {
		return [ \Elementor\Modules\DynamicTags\Module::TEXT_CATEGORY ];
	}
	/**
	* Register Controls
	*
	* Registers the Dynamic tag controls
	*
	* @since 2.0.0
	* @access protected
	*
	* @return void
	*/
	protected function _register_controls() {
		$variables = [];
		foreach ( array_keys( $_SERVER ) as $variable ) {
			$variables[ $variable ] = ucwords( str_replace( '_', ' ', $variable ) );
		}
		$this->add_control(
			'param_name',
			[
				'label' => __( 'Param Name', 'elementor-pro' ),
				'type' => \Elementor\Controls_Manager::SELECT,
				'options' => $variables,
			]
		);
	}
	/**
	* Render
	*
	* Prints out the value of the Dynamic tag
	*
	* @since 2.0.0
	* @access public
	*
	* @return void
	*/
	public function render() {
		$param_name = $this->get_settings( 'param_name' );
        	if ( ! $param_name ) {
			return;
		}
		if ( ! isset( $_SERVER[ $param_name ] ) ) {
			return;
		}
	
		$value = $_SERVER[ $param_name ];
		echo wp_kses_post( $value );
	}
}
```

#### Register the Dynamic Tag

So after we have our dynamic tag class ready all that we have to do is register the tag with Elementor’s Dynamic tag manager at the `elementor/dynamic_tags/register_tags` hook:

```
add_action( 'elementor/dynamic_tags/register_tags', function( $dynamic_tags ) {
	// In our Dynamic Tag we use a group named request-variables so we need 
	// To register that group as well before the tag
	\Elementor\Plugin::$instance->dynamic_tags->register_group( 'request-variables', [
		'title' => 'Request Variables' 
	] );
	// Include the Dynamic tag class file
	include_once( 'path/to/dynamic/tag/class/file' );
	// Finally register the tag
	$dynamic_tags->register_tag( 'Elementor_Server_Var_Tag' );
} );
```

#### Final Notes on Creating Dynamic Tags

- You should only include the Dynamic Tag class on the `elementor/dynamic_tags/register_tags` hook to make sure Elementor’s autoloader loads all base classes for you.
- For URL, Image, Media and Gallery controls, you need to extend `Elementor\Core\DynamicTags\Data_Tag` instead.  
  There are many types of controls you can add to your widget to make it easier to configure. We have a separate section with a full list of available controls.
